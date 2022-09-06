var callBackGetSuccess =function fakeDetector(data) {
    console.log(data.main)
    document.getElementById("test").innerText = data
}

async function fetchText(url) {

    var url = url

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
