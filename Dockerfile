FROM python:3.10

# WORKDIR /app

COPY requirements.txt requirements.txt
COPY ./app /app

RUN pip3 install -r requirements.txt

ARG model_folder=/root/.cache/torch/sentence_transformers/sentence-transformers_all-MiniLM-L12-v2
ARG model_repository=https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2

# if you want to download only the model
# ARG model_url=https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2/resolve/main/pytorch_model.bin
# RUN mkdir -p ${model_folder}
# RUN curl -L ${model_url} --output ${model_folder}/pytorch_model.bin

# this way we download the model during build time and heat up the cache. So we don't have to download
# it every time we start the instance
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get install git-lfs
RUN mkdir -p ${model_folder}
RUN git lfs clone ${model_repository} ${model_folder}
# git lfs clone https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2 /root/.cache/torch/sentence_transformers/sentence-transformers_all-MiniLM-L12-v2

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]