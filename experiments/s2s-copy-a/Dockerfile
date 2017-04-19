FROM node:boron

RUN apt-get update
RUN apt-get -y install curl build-essential git pkg-config
RUN apt-get -y install libcairo2-dev libjpeg-dev libgif-dev

RUN npm install -g nodeunit esprima grunt browserify uglifyjs mongodb
RUN npm install -g probmods/webppl#6a9f96f0faea0b2095d968b3e1657c8655e553f7

RUN mkdir -p ~/.webppl
RUN npm install --prefix ~/.webppl webppl-timeit webppl-dp webppl-json
RUN npm install --prefix ~/.webppl null-a/webppl-nn#old-interface
RUN npm install --prefix ~/.webppl null-a/webppl-fs#1801afea46148aceace9cf3fd983ae928747df04

RUN mkdir /data
RUN mkdir /data/logs
RUN mkdir /data/config
RUN mkdir /data/results

ENV project_git_url https://github.com/stuhlmueller/dialog.git
ENV experiment_cmd "WEBPPL_PARAM_PATH=/data/results/ webppl --require webppl-nn --require webppl-fs --require models/common/ --param-store file --param-id s2s-copy-1 --random-seed 10 models/s2s-copy.wppl"

CMD if [ ! -d "/project" ]; then \
      git clone ${project_git_url} /project; cd /project/models/common; npm install; \
    fi && \
    cd /project && \
    if [ -w /data/ ]; then \
      git log -1 > /data/config/git.txt && \
      echo "$OPTIONS" > /data/config/options.txt; \
    fi && \
    eval "$experiment_cmd $OPTIONS"