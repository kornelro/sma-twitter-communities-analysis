if [ $1 = "clear" ]; then
    docker container prune
    docker rmi sma3_scraper
    docker build -t sma3_scraper .
    SEARCH_DEPTH=$2
else
    SEARCH_DEPTH=$1
fi

docker run --mount type=bind,source=/home/kornel/Projects/SMA/assignment-3-kornelro/data,target=/home/scrapped_data sma3_scraper python3 scraper.py --search-depth $SEARCH_DEPTH