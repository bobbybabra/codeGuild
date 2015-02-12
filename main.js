function addListItem() {
    // create a new List Item
    var li = document.createElement("li");
    // create some text
    //var t = document.createTextNode("Money");
    var things = ['Money', 'Cars', 'Clothes', 'Nature', 'Food', 'Friends', 'Fitness'];
var thing = things[Math.floor(Math.random()*things.length)];
var t = document.createTextNode(thing);
    // assign the text value to the new list item
    li.appendChild(t);
    // get all the elements of class list (which is exactly 1 in this example)
    var ol = document.getElementsByClassName("list");
    // target the one and only element and append the new list item to the exis$
    ol[0].appendChild(li);
}


