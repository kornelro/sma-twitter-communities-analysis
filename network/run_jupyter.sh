if [ $1 = "clear" ]; then
    docker container prune
    docker rmi sma3_network
    docker build -t sma3_network .
fi

docker run -p 8888:8888 \
--mount type=bind,source=/home/kornel/Projects/SMA/sma-twitter-communities-analysis/network/notebooks,target=/home/work \
--mount type=bind,source=/home/kornel/Projects/SMA/sma-twitter-communities-analysis/data,target=/home/data \
--mount type=bind,source=/home/kornel/Projects/SMA/sma-twitter-communities-analysis/gephi,target=/home/gephi \
sma3_network jupyter-notebook --notebook-dir="./home/work" --ip=0.0.0.0 --allow-root --NotebookApp.token='abc'