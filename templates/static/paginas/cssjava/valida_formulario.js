const tx_nome = document.getElementById("tx-nome");
const tx_email = document.getElementById("tx-email");
const bt_enviar = document.getElementById("bt-enviar");
const p_erros = document.getElementById("msg-erros");

function validar_nome() {
	if (tx_nome.value.trim() == "") {
		p_erros.innerText = "O nome não pode ser vazio";
		return false;
	}
	return true;
}

function validar_email() {
	if (tx_email.value.trim() == "") {
		p_erros.innerText = "O e-mail não pode ser vazio";
		return false;
	}
	return true;
}

bt_enviar.addEventListener("click", function(event){
	// se qualquer uma das duas funções devolver false, o if será verdadeiro
	if (!validar_nome() || !validar_email()) {
		alert("Preencha os campos obrigatórios!");
		event.preventDefault(); // cancela a ação padrão do botão enviar (ou seja, não envia o formulário)
	}
});

tx_nome.addEventListener("focusout", function() {
	validar_nome();
});

tx_email.addEventListener("focusout", function () {
	validar_email();
});