function addCount(id) {

  id_name = "count_" + id;

  count = Number(document.getElementById(id_name).value);
  document.getElementById(id_name).value = count + 1;

}

function subCount(id) {

  id_name = "count_" + id;

  count = Number(document.getElementById(id_name).value);

  if (count > 0) {
    document.getElementById(id_name).value = count - 1;
  }

}

function displayChange() {

  const table = document.getElementById('table').value;

  if (table != "None") {
    document.getElementsByClassName('disNone')[0].style.display = "block";
    document.getElementsByClassName('disNone')[1].style.display = "block";
    document.getElementsByClassName('disNone')[2].style.display = "block";
  } else {
    document.getElementsByClassName('disNone')[0].style.display = "none";
    document.getElementsByClassName('disNone')[1].style.display = "none";
    document.getElementsByClassName('disNone')[2].style.display = "none";
  }

}