# Use rocker/verse base image
ARG base_tag="3.5.3"
FROM rocker/verse:${base_tag}

# add packages
RUN Rscript -e 'devtools::install_version("xgboost", version = "0.90.0.2", upgrade = "never", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_version("forecast", version = "8.10", upgrade = "never", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_version("MatchIt", version = "3.0.2", upgrade = "never", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_version("plotly", version = "4.9.1", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_version("caret", version = "6.0-84", upgrade = "never", repos = "http://cran.us.r-project.org")'

ARG data_volume=/data
RUN mkdir ${data_volume} && \
    chmod 777 ${data_volume}

# launch rstudio in browser as default
WORKDIR /home/rstudio
