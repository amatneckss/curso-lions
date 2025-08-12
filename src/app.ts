

console.log('Hello, tipescript!')
let nome: String = 'valentina'
console.log(nome)
nome = 'marco'
console.log(nome)

let number: number = 2000
console.log(number)

let boolean: boolean = true
console.log(boolean)

let array: string[] =  ['cor','tamanho']
console.log(array)

let tupla: [number, boolean, string] = [20,true,'allow']
console.log(tupla)

enum status {Pendente, Processando, Entregue, Cancelado}
let st: status = status.Entregue 
console.log(status); 

let tupla2: [string, number] = ["O produto X custa R$ y",0] 
function descricao(nome:string,preco:number){
return 'nome do produto: '+ nome + ' ,preco:'+ preco
} 
console.log(descricao('notebook',2000))
console.log(descricao('mouse',400))

interface iUser{
    id: number
    name: string
    email: string
    isActive: boolean
}

type UserRole = 'admin'| 'editor'| 'viewer'

interface IAdminUser extends iUser {
    role: UserRole
}

const iUser: iUser = {
    email: '@teste',
    id: 22,
    isActive: true,
    name: 'valen'   
}

console.log(iUser)
    
function exibir (usuario: iUser){
    console.log('nome: '+usuario.name)
    console.log('idade: '+usuario.id)
    console.log('isActive: '+usuario.isActive)
    console.log('email: '+usuario.email)
}

exibir(iUser)

function getData<T>(items: T[]): T[]{
    return items; 
}
const stringarray = getData<string>(['a','b','c']);
console.log('array de string:',stringarray)

const numberarray = getData<number>([1,2,3,]);
console.log('arrays de numero',numberarray)

const objetosarray = getData<iUser>([
    { id:1, name: 'valen', email: 'valen@email.com', isActive: true}
]);
console.log('usuarios:',objetosarray)

function getById1<T extends { id: number }>(items: T[], id: number): T | undefined
    {
        return items.find(item => item.id===id)
    }

const idarray= getById1([{ id:2, name: 'valen', email: 'valen@email.com', isActive: true, }],2)
console.log(idarray)

function getById2<T extends { id: number, name:string }>(items: T[], id: number, name: string): T | undefined
    {
        return items.find(item => item.id===id && item.name===name)
        
    }

const pessoa: iUser[]=[{ id:1, name: 'valen', email: 'valen@email.com', isActive: true, },{name:'teste',id:4,isActive: true,email: 'teste'}]
    const idarray2= getById2(pessoa,1, 'valen')
console.log(idarray2)



        



