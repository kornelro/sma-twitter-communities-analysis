if [ $1 == "clear" ];
then
    docker container prune
    docker rmi sma3_sentiment
    docker build -t sma3_sentiment .
fi

docker run \
--mount type=bind,source=/home/kornel/Projects/SMA/assignment-3-kornelro/data/23_17_38_2/users,target=/home/data \
sma3_sentiment python3 polarity.py