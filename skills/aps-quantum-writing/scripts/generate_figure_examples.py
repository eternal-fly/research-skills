"""Render illustrative appearance samples. ALL VALUES ARE SYNTHETIC.
Run: python scripts/generate_figure_examples.py --out assets/figure-examples
No smoothing, fitting, data deletion or uncertainty inference is performed.
"""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from aps_figure_style import style, size, panel, export, COLORS


def axes_finish(ax, xlabel, ylabel):
    ax.set(xlabel=xlabel, ylabel=ylabel)
    # Math subscripts use about 70% size: increase affected label to retain height.
    for label, text in ((ax.xaxis.label, xlabel), (ax.yaxis.label, ylabel)):
        if '_' in text:
            label.set_fontsize(12)
    ax.xaxis.set_major_locator(MaxNLocator(4))
    ax.yaxis.set_major_locator(MaxNLocator(4))


def note(fig):
    fig.text(.99, .005, 'Synthetic example', ha='right', va='bottom', fontsize=9, color='#444444')


def run(out):
    out = Path(out)
    with style():
        t = np.linspace(0, 5, 101)
        # PRL: vertically paired evidence; same scale, no redundant legends.
        fig, axs = plt.subplots(2, 1, figsize=size('prl'), sharex=True)
        fig.subplots_adjust(left=.21, right=.96, bottom=.13, top=.98, hspace=.12)
        for ax, gamma, letter in zip(axs, (.25, .6), ('a', 'b')):
            ax.plot(t, np.exp(-gamma*t), label=fr'$\gamma/J={gamma}$')
            ax.plot(t[::10], np.exp(-gamma*t[::10])*.94, 's', color=COLORS[1],
                    markersize=4, markerfacecolor='white', label='Comparison')
            axes_finish(ax, '', r'$P_1$')
            ax.set_ylim(-.05, 1.27)
            panel(ax, letter)
            ax.text(.95, .94, fr'$\gamma/J={gamma}$', transform=ax.transAxes, ha='right', va='top')
        axs[1].set_xlabel(r'Time $Jt$')
        axs[1].legend(loc='upper right', bbox_to_anchor=(1,.8), labels=['Model', 'Comparison'])
        note(fig); export(fig, out/'prl_compact', formats=('pdf','png','eps')); plt.close(fig)

        # PRA: actual point positions shown; bars explicitly illustrative SD.
        fig, ax = plt.subplots(figsize=size('pra'))
        fig.subplots_adjust(left=.21, right=.96, bottom=.23, top=.97)
        x = np.arange(7)
        y = np.array([.13,.26,.46,.64,.78,.85,.89])
        sd = np.array([.03,.04,.04,.03,.03,.025,.02])
        ax.errorbar(x,y,yerr=sd,fmt='o',color=COLORS[0],label=r'Mean $\pm$ SD',
                    elinewidth=.8,capthick=.7)
        ax.plot(x, .92/(1+np.exp(-(x-2))), '--', color=COLORS[1],label='Reference')
        axes_finish(ax,r'Detuning $\Delta/\kappa$',r'Population $P_e$')
        ax.set_ylim(0,1.25); ax.legend(loc='upper left'); note(fig)
        export(fig,out/'pra_errorbars', formats=('pdf','png','eps')); plt.close(fig)

        # PRB: matched heatmap scales; bin boundaries preserved (no interpolation).
        fig, axs = plt.subplots(1,2,figsize=size('prb'))
        fig.subplots_adjust(left=.085,right=.86,bottom=.22,top=.94,wspace=.27)
        k = np.linspace(-1,1,61); e = np.linspace(-2,2,81)
        K,E=np.meshgrid(k,e)
        for ax, gap, letter in zip(axs,(.25,.75),('a','b')):
            z=np.exp(-((E-np.sqrt(K*K+gap*gap))/.17)**2)+np.exp(-((E+np.sqrt(K*K+gap*gap))/.17)**2)
            im=ax.imshow(z,origin='lower',extent=(-1,1,-2,2),aspect='auto',
                         cmap='cividis',vmin=0,vmax=1,interpolation='none',rasterized=True)
            axes_finish(ax,r'Momentum $k a/\pi$',r'Energy $E/J$')
            txt=panel(ax,letter); txt.set_color('white')
        cax=fig.add_axes([.90,.22,.018,.72]); cb=fig.colorbar(im,cax=cax)
        cb.set_label(r'$A(k,E)$ (arb. units)'); cb.set_ticks([0,.5,1])
        note(fig); export(fig,out/'prb_heatmaps', formats=('pdf','png','eps')); plt.close(fig)

        # PRX Quantum: tutorial-friendly linked evidence, not a compulsory layout.
        fig,axs=plt.subplots(2,2,figsize=size('prx-quantum'))
        fig.subplots_adjust(left=.095,right=.88,bottom=.12,top=.97,hspace=.45,wspace=.37)
        ax=axs[0,0]
        for i,(err,marker,ls) in enumerate(zip((.02,.05),('o','s'),('-','--'))):
            d=np.arange(1,9); p=(1-err)**d
            ax.plot(d,p,ls,marker=marker,color=COLORS[i],label=fr'$\epsilon={err}$')
        axes_finish(ax,'Circuit depth',r'Fidelity $F$'); ax.set_ylim(.55,1.13)
        ax.legend(loc='lower left')
        ax=axs[0,1]; q=np.linspace(0,1,21)
        ax.plot(q,.15+.75*q,color=COLORS[0],label='Protocol A')
        ax.plot(q,.2+.55*q,'--',color=COLORS[1],label='Protocol B')
        axes_finish(ax,'Control fraction',r'Success $P_s$');ax.set_ylim(0,1.1)
        ax.legend(loc='lower right')
        ax=axs[1,0]; n=np.arange(1,7)
        ax.errorbar(n,.05*n,yerr=.015*np.ones(6),fmt='o',color=COLORS[0],elinewidth=.8)
        axes_finish(ax,'Noise strength (arb. units)',r'Infidelity $1-F$');ax.set_ylim(0,.4)
        ax.text(.95,.95,r'$\pm 1$ SD',transform=ax.transAxes,ha='right',va='top')
        ax=axs[1,1]; delta=np.outer(np.linspace(-1,1,20),np.linspace(-1,1,20))
        im=ax.imshow(delta,origin='lower',extent=(0,1,0,1),cmap='RdBu_r',vmin=-1,vmax=1,
                     interpolation='none',aspect='auto',rasterized=True)
        # Signed contours keep positive/negative regions identifiable in grayscale.
        cs=ax.contour(np.linspace(0,1,20),np.linspace(0,1,20),delta,
                      levels=[-.5,.5],colors='black',linewidths=.7,linestyles=['--','-'])
        ax.clabel(cs,fmt='%+.1f',fontsize=9,inline=True)
        axes_finish(ax,'Control fraction',r'Coupling $g/J$')
        cb=fig.colorbar(im,ax=ax,fraction=.045,pad=.03);cb.set_label(r'$\Delta F$');cb.set_ticks([-1,0,1])
        for ax,letter in zip(axs.flat,'abcd'):
            tag=panel(ax,letter)
            if letter=='d': tag.set_color('white')
        note(fig);export(fig,out/'prx_quantum_multipanel', formats=('pdf','png','eps'));plt.close(fig)

        # Compact table visual: use native LaTeX tabular in the actual manuscript.
        fig,ax=plt.subplots(figsize=size('pra',height_mm=44));ax.axis('off')
        fig.subplots_adjust(left=.04,right=.96,bottom=.16,top=.97)
        rows=[['A','0.932','0.012'],['B','0.907','0.018'],['C','0.884','0.021']]
        tab=ax.table(cellText=rows,colLabels=['Protocol',r'Mean $F$',r'SD'],loc='center',
                     cellLoc='right',colLoc='right',colWidths=[.38,.34,.25])
        tab.auto_set_font_size(False);tab.set_fontsize(9);tab.scale(1,1.35)
        for (r,c),cell in tab.get_celld().items():
            cell.visible_edges='';cell.set_linewidth(.6);cell.set_facecolor('white')
            if c==0:cell.get_text().set_ha('left')
            if r==0:cell.visible_edges='BT';cell.get_text().set_fontweight('bold')
            if r==len(rows):cell.visible_edges='B'
        # Match the full APS guide: paired top/bottom rules, single header separator.
        fig.canvas.draw()
        cells=tab.get_celld(); top=cells[(0,0)].get_y()+cells[(0,0)].get_height()
        bottom=cells[(len(rows),0)].get_y()
        left=cells[(0,0)].get_x(); right=cells[(0,2)].get_x()+cells[(0,2)].get_width()
        for y in (top+.018, bottom-.018):
            ax.plot([left,right],[y,y],transform=ax.transAxes,color='black',lw=.6,clip_on=False)
        note(fig);export(fig,out/'compact_table', formats=('pdf','png','eps'));plt.close(fig)

        # A contact sheet for browsing only: never use it as the manuscript figure.
        files=['prl_compact','pra_errorbars','prb_heatmaps','prx_quantum_multipanel','compact_table']
        fig,axs=plt.subplots(3,2,figsize=(10,10.5))
        for ax,name in zip(axs.flat,files):
            ax.imshow(plt.imread(out/(name+'.png')));ax.set_title(name.replace('_',' '),fontsize=12);ax.axis('off')
        axs.flat[-1].axis('off');axs.flat[-1].text(.05,.7,'All data are synthetic.\nShared APS base; flexible profiles.\nNative PDF/PNG files are separate.',fontsize=13,va='top')
        fig.tight_layout();fig.savefig(out/'style_overview.png',dpi=160);plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',default='assets/figure-examples')
    run(p.parse_args().out)
