"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
console.log('Hello, tipescript!');
let nome = 'valentina';
console.log(nome);
nome = 'marco';
console.log(nome);
let number = 2000;
console.log(number);
let boolean = true;
console.log(boolean);
let array = ['cor', 'tamanho'];
console.log(array);
let tupla = [20, true, 'allow'];
console.log(tupla);
var status;
(function (status) {
    status[status["Pendente"] = 0] = "Pendente";
    status[status["Processando"] = 1] = "Processando";
    status[status["Entregue"] = 2] = "Entregue";
    status[status["Cancelado"] = 3] = "Cancelado";
})(status || (status = {}));
let st = status.Entregue;
console.log(status);
let tupla2 = ["O produto X custa R$ y", 0];
function descricao(nome, preco) {
    return 'nome do produto: ' + nome + ' ,preco:' + preco;
}
console.log(descricao('notebook', 2000));
console.log(descricao('mouse', 400));
const iUser = {
    email: '@teste',
    id: 22,
    isActive: true,
    name: 'valen'
};
console.log(iUser);
function exibir(usuario) {
    console.log('nome: ' + usuario.name);
    console.log('idade: ' + usuario.id);
    console.log('isActive: ' + usuario.isActive);
    console.log('email: ' + usuario.email);
}
exibir(iUser);
function getData(items) {
    return items;
}
const stringarray = getData(['a', 'b', 'c']);
console.log('array de string:', stringarray);
const numberarray = getData([1, 2, 3,]);
console.log('arrays de numero', numberarray);
const objetosarray = getData([
    { id: 1, name: 'valen', email: 'valen@email.com', isActive: true }
]);
console.log('usuarios:', objetosarray);
function getById1(items, id) {
    return items.find(item => item.id === id);
}
const idarray = getById1([{ id: 2, name: 'valen', email: 'valen@email.com', isActive: true, }], 2);
console.log(idarray);
function getById2(items, id, name) {
    return items.find(item => item.id === id && item.name === name);
}
const pessoa = [{ id: 1, name: 'valen', email: 'valen@email.com', isActive: true, }, { name: 'teste', id: 4, isActive: true, email: 'teste' }];
const idarray2 = getById2(pessoa, 1, 'valen');
console.log(idarray2);
//# sourceMappingURL=app.js.map