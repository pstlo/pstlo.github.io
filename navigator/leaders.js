function displayLeaders() {
    fetch('https://us-east-2.aws.data.mongodb-api.com/app/data-nvbnb/endpoint/data/v1')
        .then(response => response.json())
        .then(data => {
            const collectionDataElement = document.getElementById('collection-data');
            collectionDataElement.innerHTML = JSON.stringify(data);
        })
        .catch(error => console.error(error));
}
