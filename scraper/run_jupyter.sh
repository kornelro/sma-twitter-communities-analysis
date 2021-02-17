if [ $1 == "clear" ];
then
    docker container prune
    docker rmi sma3_scraper
    docker build -t sma3_scraper .
fi

docker run -p 8888:8888 --mount type=bind,source=/home/kornel/Projects/SMA/assignment-3-kornelro/scraper/notebooks,target=/home/work sma3_scraper jupyter-notebook --notebook-dir="./home/work" --ip=0.0.0.0 --allow-root --NotebookApp.token='abc'