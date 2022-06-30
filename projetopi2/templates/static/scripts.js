function sair(){
    window.location = "/"
}

function teste(){
    alert("entrou no javascript")
}


function logar(){
    window.location.replace ("login")
}


//----------Funções de Cadastro----------\\

function cadPrestador(){
    window.location = "cadPrestador"
}



//----------Funções de Edição----------\\ 
function editFunc(){
    window.location = "editFunc"
}



//----------Funções de Edição----------\\ 
function deleteFunc(){
    window.location = "deleteFunc"
}


//----------Funções para listar Logins----------\\
function listaLogin(){
    window.location.replace("listaPrestador")
}

function listaPrestador(){
    window.location.replace("listaPrestador")
}

function listaTecnologia(){
    window.location = "listaTecnologia"
}


//--------------------Evento para mostrar/esconder senha--------------------\\
document.getElementById('olho').addEventListener('mousedown', function() {
    document.getElementById('id_password1').type = 'text';
  });
  
  document.getElementById('olho').addEventListener('mouseup', function() {
    document.getElementById('id_password1').type = 'password';
  });
  
  // Para que o password não fique exposto apos mover a imagem.
  document.getElementById('olho').addEventListener('mousemove', function() {
    document.getElementById('id_password1').type = 'password';
  });
//------------------Fim do Evento para mostrar/esconder senha------------------\\

$("#telefone").mask("(00) 0000-0000");
$("#celular").mask("(00) 0000-0000");


function areaAdmin(){
    const senha = document.querySelector("#senha");
    const nome = document.querySelector("#nome");
    const vNome = nome.value;
    const vSenha = senha.value;
    if(vNome=="" || vSenha==""){
        alert("um dos campos esta vazio!")
    }
    else{
        if(vNome=="admin" & vSenha=="1234"){
            window.location.replace("adminarea")
        }
        else{
            window.location.replace("areadoador")
        }
    }
}



function verificar(){
    senha1 = document.getElementById('senha1').value;
    senha2 = document.getElementById("senha2").value;
    if(senha1 != senha2){
        alert('senhas não coincidem!');
    }
    else{
        document.FormSenha.submit();
    }
}


/*var id_password1 = document.getElementById("id_password1")
  , id_password2 = document.getElementById("id_password2")
  , cadastrar = document.getElementById("cadastrar");

function validatePassword(){
  if(id_password1.value != id_password2.value) {
    id_password2.setCustomValidity("Senhas diferentes!");
  } else {
    id_password2.setCustomValidity('');
  }
}

id_password1.onchange = validatePassword();
id_password2.onkeyup = validatePassword();

cadastrar.onclick = validatePassword();



function consultaCep(){
    var cep = document.getElementById("cep").value.replace(/\D/g, '');
    var url = 'https://viacep.com.br/ws/'+$cep+'/json/';
    var retorno = new XMLHttpRequest();

    retorno.open('GET', url);
    retorno.onerror = finction(e){ 
        document.getElementById('return').innerHTML = 'API offline/cep invalido!'
    }

    retorno.onload = () =>{
        var resposta = JSON.parse(retorno.responseText);

        if (resposta.erro === true){
            document.getElementById('return').innerHTML = 'Cep não encontrado!';
        }else{
            document.getElementById('return').innerHTML = 'CEP:'+response.cep+'<br>'+
            'Logradouro:'+ response.logradouro + '<br>'+ 'Bairro: '+ response.bairro +'<br>'+
            'Cidade/UF: '+response.localidade+' / '+ response.uf;
        }
    }
    request.send();
}

*/

