FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime
WORKDIR /usr/src/app/
COPY requirements.txt ./

RUN apt-get update && apt-get upgrade -y && apt-get clean
# Python package management and basic dependencies
RUN apt-get install -y curl python3.7 python3.7-dev python3.7-distutils
# Register the version in alternatives
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
# Set python 3 as the default python
RUN update-alternatives --set python /usr/bin/python3.7
# Upgrade pip to latest version
RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py --force-reinstall && \
    rm get-pip.py
RUN apt-get install -y libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev

# install ffmpeg
RUN apt install ffmpeg -y
RUN pip install -U pip
RUN pip install -U setuptools
RUN pip install https://github.com/kpu/kenlm/archive/master.zip
RUN pip install -r requirements.txt
# RUN pip install jupyter

# normalization tools
RUN apt-get install -y libsndfile1
RUN pip install Cython
RUN pip install "nemo_toolkit[all]"
RUN pip install pynini
RUN apt install -y wget
RUN apt-get install build-essential -y
RUN wget http://www.openfst.org/twiki/pub/FST/FstDownload/openfst-1.7.3.tar.gz
RUN tar -xvf openfst-1.7.3.tar.gz
RUN chown -R root:root openfst-1.7.3
WORKDIR /usr/src/app/openfst-1.7.3
RUN ./configure --enable-grm
RUN make && make install
WORKDIR /usr/src/app
COPY . ./

# CMD jupyter notebook --ip 0.0.0.0 --allow-root
# ENTRYPOINT [ "python", "./app.py" ]
ENTRYPOINT ["gunicorn"  , "-b", "0.0.0.0:8050", "app:server", "--timeout", "600"]