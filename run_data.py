{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOVl1FJRAJaEvf8i1OCAF/E",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/VCosmo/POLOSA/blob/main/run_data.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os, sys\n",
        "import pandas as pd\n",
        "import pickle\n",
        "from scipy.integrate import cumtrapz\n",
        "import scipy\n",
        "\n",
        "from gal4H0 import *\n",
        "\n",
        "cosmo=FlatLambdaCDM(H0=70.,Om0=0.25)\n",
        "\n",
        "# Define the path to the catalog compressed CSV file:\n",
        "catalog_filename = \"/content/drive/MyDrive/13826.csv.bz2\"  \n",
        "# Define the list of columns that uniquely identify each row\n",
        "data = pd.read_csv(catalog_filename, sep=\",\", comment='#', na_values=r'\\N', compression='bz2')\n",
        "abs_M=data['abs_mag_r'].to_numpy()[0:1000:]\n",
        "galaxies_list=data['z'].to_numpy()[0:1000:]\n",
        "Labs=M2L(abs_M)\n",
        "app_m=M2m(abs_M, cosmo.luminosity_distance(galaxies_list).to('Mpc').value)\n",
        "print(len(app_m))\n",
        "sys.path.append('../')\n",
        "\n",
        "np.random.seed(0)\n",
        "\n",
        "filename=['6_0_10perc_acc.p' ,'6_1_10perc_acc.p' ,'6_2_10perc_acc.p']\n",
        "\n",
        "beta=1\n",
        "betas=[beta-1, beta, beta+1]\n",
        "\n",
        "Ngw=100\n",
        "sigma_dl=0.1\n",
        "zcut_rate=1.4\n",
        "dl_thr=1550\n",
        "H0_array=np.linspace(40,120,2000)\n",
        "Nrep=20\n",
        "\n",
        "for j in range(3):\n",
        "\n",
        "  output={'H0_grid':H0_array,\n",
        "       'single_pos':[],\n",
        "       'true_H0':np.zeros(Nrep)}\n",
        "\n",
        "  for ii in tqdm(range(Nrep)):\n",
        "    output['true_H0'][ii]=np.random.uniform(40,120,size=1)\n",
        "    true_cosmology = FlatLambdaCDM(H0=output['true_H0'][ii],Om0=0.25)\n",
        "    gw_obs_dl,_,_,std_dl=draw_gw_events_L(Ngw,sigma_dl,dl_thr,galaxies_list,true_cosmology,zcut_rate, Labs, beta)\n",
        "    posterior_matrix,combined=galaxy_catalog_analysis_accurate_redshift_L(H0_array,galaxies_list,zcut_rate,gw_obs_dl,sigma_dl,dl_thr,app_m,betas[j])\n",
        "    output['single_pos'].append(posterior_matrix)\n",
        "    \n",
        "  pickle.dump(output,open(filename[j],'wb'))"
      ],
      "metadata": {
        "id": "jD8WmJvOKWhJ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}