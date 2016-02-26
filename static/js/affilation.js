

console.log("this is a test");

function successHandler(results) {
    console.log(results);
}

function getAffiliations() {
    $.get('/affiliations.json', successHandler);
    console.log("Finished sending AJAX");
}


getAffiliations();