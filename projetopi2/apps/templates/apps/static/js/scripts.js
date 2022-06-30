function sair(){
    window.location = "/"
}

function teste(){
    alert("entrou no javascript")
}

function sairAdmin() {
    window.history.back()
}

function sairADM(){
    window.location.replace("adminarea")
}

function logar(){
    window.location.replace ("login")
}


//----------Funções de Cadastro----------\\
function cadDonat(){
    window.location = "cadDonat"
}

function cadPrestador(){
    window.location = "cadPrestador"
}

function cadDoador(){
    window.location = "cadDoador"
}

function cadFunc(){
    window.location = "cadFunc"
}



//----------Funções de Edição----------\\ 
function editFunc(){
    window.location = "editFunc"
}



//----------Funções de Edição----------\\ 
function deletePrestador(){
    window.location = "deletePrestador"
}

function deleteDonat(){
    window.location = "deletePrestador"
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
/*document.getElementById('olho').addEventListener('mousedown', function() {
    document.getElementById('senha').type = 'text';
  });
  
  document.getElementById('olho').addEventListener('mouseup', function() {
    document.getElementById('senha').type = 'password';
  });
  
  // Para que o password não fique exposto apos mover a imagem.
  document.getElementById('olho').addEventListener('mousemove', function() {
    document.getElementById('senha').type = 'password';
  });*/
//------------------Fim do Evento para mostrar/esconder senha------------------\\

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
