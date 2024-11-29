FROM continuumio/miniconda3

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    curl \
    && apt-get clean

# Python環境のセットアップ
COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml && conda clean -afy

# .bashrc にアクティベーションを追加
RUN echo "conda activate Python-Scraping-MachineLearning_env" >> ~/.bashrc

# SHELL をログインシェルに設定
SHELL ["/bin/bash", "-l", "-c"]

# 作業ディレクトリの設定
WORKDIR /app

# コンテナ起動時のデフォルトシェル
CMD ["/bin/bash"]