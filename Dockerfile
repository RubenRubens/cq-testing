FROM continuumio/miniconda3
RUN apt install -y libgl1-mesa-glx
RUN conda install conda-build
RUN apt-get install -y git
WORKDIR /
RUN git clone https://github.com/cadquery/cadquery.git
WORKDIR /cadquery
RUN git pull origin master
RUN conda env create -n cq -f environment.yml
RUN echo "source activate cq" > ~/.bashrc
ENV PATH /opt/conda/envs/cq/bin:$PATH
WORKDIR /testing
