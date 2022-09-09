var callBackGetSuccess =function fakeDetector(data) {
    console.log(data)
    document.getElementById("text").innerText = data.fiability + " fiable !"
    document.getElementById("linkIsSafe").innerText = "Le lien est sécurisé : " + (data.info.urlIsSafe ? "Oui !" : "non")
    document.getElementById("authorFound").innerText = "Un auteur à été trouvé  : " + (data.info.authorFound ? "Oui !" : "non")
    document.getElementById("authorLink").innerText = "L'auteur possède une page web : " + (data.info.authorLink ? "Oui !" : "non")
    document.getElementById("subjectFound").innerText = "Sujet trouvé : " + data.info.subjectFound


    const divContent = []

    for(let i = 0; i < data.info.webLink.length; i++){
        const balise = '<a class="link" target="_blank" href= "' + data.info.webLink[i] + '" > lien ' + (i+1) +  ' : ' + data.info.webLink[i] +' </a>'
        divContent.push(balise)
    }
    document.getElementById("allLinks").innerHTML = "Liens trouvé sur des sites fiables en rapport avec l'article :  "
    document.getElementById("allLinks").innerHTML += '</br> </br>'
    for(let i = 0; i < divContent.length; i++){
        document.getElementById("allLinks").innerHTML += divContent[i] + '<hr>'
    }


}

async function fetchText(url) {

    var url = "http://127.0.0.1:5000/?url=" + url

    $.get(url, callBackGetSuccess).done(function () {
        //alert( "second success" );
    })
        .fail(function () {
            alert("error");
        })
        .always(function () {
            //alert( "finished" );
        });


}

async function getFiablity() {
    const url = document.getElementById("inputLink").value

    await fetchText(url)
}
