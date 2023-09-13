function displayChange() {

  const menu = document.getElementById('menu').value;

  if (menu != "None") {
    document.getElementsByClassName('disNone')[0].style.display = "block";
  } else {
    document.getElementsByClassName('disNone')[0].style.display = "none";
  }

}