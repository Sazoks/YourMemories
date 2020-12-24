// Проверяем, поставил ли юзер метку на карте.
document.getElementById("send_btn").onclick = function() {
    if (document.getElementById("id_place").value == '') {
        alert("Выберите место на карте!");
        return;
    }
    document.getElementById("send_btn").type = "submit";
}