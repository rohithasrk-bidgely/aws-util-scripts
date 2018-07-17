import boto3


def get_queues_without_suffix():
    client = boto3.client('sqs')
    queues = []
    urls = client.list_queues().get('QueueUrls')
    for url in urls:
        name = url.split('/')[-1]
        name_array = name.split('-')
        env = name_array[1]
        if len(name_array)==3:
            suffix = name_array[2]
            tags = client.list_queue_tags(QueueUrl=url).get('Tags')
            if not tags or not tags.get('QueueSuffix') == suffix:
                queues.append(url)
    return queues

if __name__ == "__main__":
    queues = get_queues_without_suffix()
    for q in queues:
        print(q)
