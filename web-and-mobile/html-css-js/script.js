window.addEventListener("load", function ()
{
    //Get button element references.
    let clickCounterElement = document.getElementById("click-counter");
    let clickButtoneElement = document.getElementById("click-button");

    //counter value
    let counter = 0;

    //click button function
    let clickButonFunction = function ()
    {
        //Increment counter
        counter++;

        //update click counter value
        clickCounterElement.innerHTML = counter;
    };

    //attach click button
    clickButtoneElement.addEventListener("click", clickButonFunction);
});