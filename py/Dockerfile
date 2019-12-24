ARG base_tag="7a0c7325e470"
FROM jupyter/scipy-notebook:${base_tag}

USER $NB_UID

# Install Python 3 packages
RUN conda install --quiet --yes \
    'conda-forge::ipdb=0.12*' \
    'conda-forge::psycopg2=2.8*' \
    'conda-forge::pylint=2.4*' \
    'conda-forge::pytest=5.3*' \
    && \
    conda clean --all -f -y && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# install some other data packages
RUN conda install --quiet --yes \
    'fbprophet=0.5*' \
    'conda-forge::airflow=1.10*' \
    && \
    conda clean --all -f -y && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# install plotly related packages
RUN conda install --quiet --yes \
    'conda-forge::dash=1.4*' \
    'conda-forge::dash-daq=0.2*' \
    'plotly::plotly=4.4*' \
    'plotly::plotly-orca=1.2*' \
    'psutil=5.6*' \
    && \
    conda clean --all -f -y && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# run the build step for jupyter lab plotly extension
RUN export NODE_OPTIONS=--max-old-space-size=4096 && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build  && \
    jupyter labextension install jupyterlab-plotly --no-build  && \
    jupyter labextension install plotlywidget --no-build  && \
#    jupyter lab build  && \
    unset NODE_OPTIONS


# port for vscode
EXPOSE 3000

# port for flask
EXPOSE 5000

# port for dash
EXPOSE 8050

# port for airflow
EXPOSE 8080

# port for jupyter
EXPOSE 8888

# port for plotly-orca
EXPOSE 9091

ARG airflow_home=/home/$NB_USER/airflow
ARG dags_home=/home/$NB_USER/airflow/dags
ARG data_volume=/home/$NB_USER/data
ARG app_home=/home/$NB_USER/app
ARG jupyter_home=/home/$NB_USER/lab
ARG utils_home=/home/$NB_USER/utils
RUN mkdir -p ${dags_home} && \
    mkdir ${data_volume} && \
    mkdir ${app_home} && \
    mkdir ${jupyter_home} && \
    mkdir ${utils_home} && \
    fix-permissions /home/$NB_USER

USER $NB_UID

# Run bash upon entry to keep alive
CMD [ "/bin/bash" ]
