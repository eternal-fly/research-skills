"""Deterministic SYNTHETIC two-mode model, not measured data or a PRL template.
Run python scripts/generate_mechanism_examples.py --out assets/mechanism-examples
kappa_a=1, kappa_b=.08 are ENERGY decay rates (full linewidths); amplitude
rates are kappa/2. A=[[ -.5-i Delta, -i g],[-i g,-.04]]. State starts (1,0).
No fitted parameters, randomness, uncertainty, Lindblad/dephasing, or novelty claims.
"""
from pathlib import Path
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.linalg import expm
from aps_figure_style import style,export,COLORS


def footprint(columns,height_mm,width_mm=None):
    """Explicit final canvas; width presets are adjustable working choices."""
    widths={'single':85.,'double':178.}
    if columns not in widths: raise ValueError('columns must be single or double')
    width=widths[columns] if width_mm is None else float(width_mm)
    if width<=0 or height_mm<=0: raise ValueError('dimensions must be positive')
    return width/25.4,height_mm/25.4


def generator(g,delta=0.):
    return np.array([[-.5-1j*delta,-1j*g],[-1j*g,-.04]],dtype=complex)


def poles(g,delta=0.):
    """Amplitude-generator eigenvalues lambda; frequencies are -Im(lambda)."""
    return np.linalg.eigvals(generator(g,delta))


def response(omega,delta,g):
    b=.04-1j*np.asarray(omega)
    return b/((.5-1j*(np.asarray(omega)-np.asarray(delta)))*b+g*g)


def evolution(t,g,delta=0.):
    # Matrix exponential also works at the exceptional point.
    A=generator(g,delta)
    return np.array([expm(A*ti)@np.array([1.,0.]) for ti in t])


def label(ax,letter):
    ax.text(0,1.04,'('+letter+')',transform=ax.transAxes,weight='bold',va='bottom')


def stamp(fig):
    fig.text(.99,.012,'Synthetic linear model',ha='right',fontsize=7,color='#555555')


def run(out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    with style():
        # Dominant field map and registered cut. Absolute intensity uses common units.
        w=np.linspace(-2,2,601);d=np.linspace(-1,1,301);g=.1
        z=abs(response(w[None,:],d[:,None],g))**2
        fig=plt.figure(figsize=footprint('double',69))
        gs=fig.add_gridspec(1,3,width_ratios=[1.75,.055,1],left=.095,right=.98,bottom=.24,top=.90,wspace=.34)
        ax=fig.add_subplot(gs[0]);cax=fig.add_subplot(gs[1]);cut=fig.add_subplot(gs[2])
        im=ax.pcolormesh(w,d,z,cmap='cividis',shading='nearest',norm=LogNorm(vmin=.01,vmax=4),rasterized=True)
        ax.axhline(0,color='white',ls='--',lw=.8)
        ax.text(.025,.91,r'Cut: $\Delta=0$',transform=ax.transAxes,color='white',fontsize=8)
        ax.set(xlabel=r'Drive frequency $\omega/\kappa_a$',ylabel=r'Detuning $\Delta/\kappa_a$')
        cb=fig.colorbar(im,cax=cax,ticks=[.01,.1,1,4]);cb.ax.tick_params(labelsize=8)
        cb.ax.set_title(r'$|a|^2$',fontsize=9,pad=9)
        cb.ax.set_yticklabels(['0.01','0.1','1','4'])
        cut.plot(w,abs(response(w,0,0))**2,'--',color=COLORS[1],label=r'$g=0$')
        cut.plot(w,abs(response(w,0,g))**2,color=COLORS[0],label=r'$g=0.1$')
        cut.set(xlim=(-.7,.7),ylim=(0,4.3),xlabel=r'$\omega/\kappa_a$',ylabel=r'$|a|^2$')
        cut.legend(loc='lower right',fontsize=8);cut.set_xticks([-.5,0,.5]);label(ax,'a');label(cut,'b');stamp(fig)
        export(fig,out/'response_map');plt.close(fig)

        # Eigenvalue trajectories are computed, not arbitrary arrows or cartoon poles.
        fig,ax=plt.subplots(figsize=footprint('single',82))
        fig.subplots_adjust(left=.24,right=.95,bottom=.22,top=.92)
        gg=np.linspace(0,.6,601)
        # Analytic branch follows exact characteristic equation at Delta=0.
        root=np.sqrt((.23**2-gg**2).astype(complex))
        for lam,col in zip((-.27+root,-.27-root),COLORS[:2]):
            ax.plot(-lam.imag,-lam.real,color=col,lw=1.5)
        for g,marker,col in [(0,'o','#555555'),(.1,'s',COLORS[2]),(.25,'^',COLORS[3])]:
            lam=poles(g);ax.scatter(-lam.imag,-lam.real,marker=marker,s=25,color=col,zorder=5,label=fr'$g={g:g}$')
        ax.plot(0,.27,'x',color='black',ms=6)
        ax.annotate(r'$g_{\rm EP}=0.23$',xy=(0,.27),xytext=(.09,.37),fontsize=8,arrowprops=dict(arrowstyle='-',lw=.6))
        ax.set(xlabel=r'Pole frequency $-\mathrm{Im}\lambda/\kappa_a$',ylabel=r'Amplitude decay $-\mathrm{Re}\lambda/\kappa_a$',xlim=(-.59,.59),ylim=(0,.55))
        ax.set_xticks([-.5,0,.5]);ax.legend(loc='upper left',fontsize=8);stamp(fig)
        export(fig,out/'pole_trajectory');plt.close(fig)

        # Time-domain cross-check: transfer and tail, with the identical uncoupled control.
        t=np.linspace(0,80,801);v=evolution(t,.1);v0=evolution(t,0)
        fig,axs=plt.subplots(1,2,figsize=footprint('double',68))
        fig.subplots_adjust(left=.095,right=.975,bottom=.24,top=.91,wspace=.33)
        axs[0].plot(t,abs(v[:,0])**2,color=COLORS[0],label=r'$|a|^2$, $g=0.1$')
        axs[0].plot(t,abs(v[:,1])**2,color=COLORS[2],label=r'$|b|^2$, $g=0.1$')
        axs[0].plot(t,abs(v0[:,0])**2,'--',color=COLORS[1],label=r'$|a|^2$, $g=0$')
        zoom=axs[0].inset_axes([.43,.25,.52,.25])
        zoom.plot(t,abs(v[:,1])**2,color=COLORS[2]);zoom.set(xlim=(0,15),ylim=(0,.025))
        zoom.set_xticks([0,5,10,15]);zoom.set_yticks([0,.02]);zoom.tick_params(labelsize=7)
        zoom.set_title(r'$|b|^2$ (zoom)',fontsize=7,pad=3)
        axs[0].set(xlim=(0,15),ylim=(0,1.04),xlabel=r'Time $\kappa_a t$',ylabel='Mode energy (normalized)');axs[0].legend(fontsize=8)
        axs[1].semilogy(t,np.sum(abs(v)**2,axis=1),color=COLORS[0],label=r'Total, $g=0.1$')
        axs[1].semilogy(t,np.sum(abs(v0)**2,axis=1),'--',color=COLORS[1],label=r'Total, $g=0$')
        axs[1].set(xlim=(0,80),ylim=(1e-8,1.2),xlabel=r'Time $\kappa_a t$',ylabel='Total energy (normalized)');axs[1].legend(fontsize=8)
        for ax,l in zip(axs,'ab'):label(ax,l)
        stamp(fig);export(fig,out/'dynamics');plt.close(fig)
    captions='''# Synthetic two-mode mechanism examples

All figures are computed from A = [[-κa/2-iΔ, -ig], [-ig, -κb/2]], with κa=1 and κb=0.08. κ denotes an energy-decay rate or full linewidth; the amplitude-decay rate is κ/2. These are pedagogical calculations, not experiments or an established novelty claim. Couplings, detunings and frequencies are in units of κa.

## response_map.pdf (178 × 69 mm working double-column canvas)
(a) Squared driven response |a(ω)|² at g=0.1 over drive frequency and bare mode-a detuning, for unit drive amplitude in normalized units. The logarithmic color scale has fixed limits 0.01–4; dashed line marks Δ=0. (b) The corresponding Δ=0 spectrum compared with the uncoupled g=0 response, retaining identical bare loss rates. The map establishes parameter dependence; the cut exposes the narrow interference feature. A spectrum alone does not locate stored energy. No incoherent-path or dephasing control is plotted because their definitions/solver outputs were not supplied.

## pole_trajectory.pdf (85 × 82 mm working single-column canvas)
Computed amplitude-generator poles at Δ=0 for 0≤g≤0.6. Vertical axis is amplitude damping, not full linewidth; horizontal axis is pole frequency. Two connected branches approach the exceptional point g=0.23 then separate in frequency at equal damping 0.27. Markers locate g=0, 0.1 and 0.25. At g=0.1 the damping rates are approximately 0.06288 and 0.47712. At g=0.25 both damping rates are 0.27: the weak-coupling slow-pole argument cannot be carried unchanged into this regime.

## dynamics.pdf (178 × 68 mm working double-column canvas)
Free evolution from a(0)=1, b(0)=0 using matrix exponentials. (a) Early-time energies show transfer into b at g=0.1 and compare a with the uncoupled control; the inset enlarges the small transferred population on the same time interval. (b) Total energy on a log scale shows the late-time tail compared with g=0. The total decreases monotonically because d(|a|²+|b|²)/dt = -κa|a|²-κb|b|². The g=0 control transfers no amplitude to b; coupling redistributes excitation without altering the bare damping parameters. Curves are deterministic model solutions, not single-shot stochastic trajectories or ensemble statistics.

## Reproduction and limits
Run python scripts/generate_mechanism_examples.py --out assets/mechanism-examples. Run python -m unittest discover -s tests. NumPy, SciPy and Matplotlib are required. PDF/PNG exports retain canvas dimensions; these widths are configurable working presets, not journal-specific aspect-ratio mandates. Do not infer error bars, noise resilience, nonlinear protection, phase transitions or a thermodynamic limit from this model. The footprint function explicitly chooses single/double width and height, independently of journal. Legacy aps_figure_style.size remains unchanged for compatibility.
'''
    (out/'captions.md').write_text(captions)
    (out/'model_provenance.json').write_text(json.dumps(dict(kind='synthetic deterministic linear model',kappa_a=1,kappa_b=.08,kappa_convention='energy decay/full linewidth; amplitude decay kappa/2',response_g=.1,dynamics_g=.1,delta_dynamics=0,initial_amplitudes=[1,0],exceptional_point=.23,amplitude_damping_g01=sorted((-poles(.1).real).tolist()),amplitude_damping_g025=(-poles(.25).real).tolist(),no_measured_data=True),indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',default='assets/mechanism-examples');run(p.parse_args().out)
