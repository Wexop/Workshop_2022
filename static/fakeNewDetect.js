var callBackGetSuccess =function fakeDetector(data) {
    console.log(data)
    document.getElementById("text").innerText = data
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
