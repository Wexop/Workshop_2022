var callBackGetSuccess =function fakeDetector(data) {
    console.log(data)
    document.getElementById("text").innerText = data.fiability
    document.getElementById("linkIsSafe").innerText = "Link is safe : " + data.info.urlIsSafe
    document.getElementById("authorFound").innerText = "Author found : " + data.info.authorFound
    document.getElementById("authorLink").innerText = "Author have a link : " + data.info.authorLink

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
