function check(id) {

  if (window.matchMedia('(max-width: 700px)').matches) {

    alert('この機能はスマホで使用できません。');
    document.getElementById(id).checked = false;

  } else if (window.matchMedia('(min-width: 700px)').matches) {

    const csrfToken = document.querySelector("input[name='csrfmiddlewaretoken']").value;

    const post = fetch("/backyard/", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({
        id: id,
      }),
    });

    location.reload();
  }

}