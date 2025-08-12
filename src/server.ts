import express from 'express';

const app = express();
const port: number = 3000;
app.use(express.json())

app.get('/index', (req, res) => {
    res.send('Bem Vindo')
})

app.listen(port, () => {
    console.log("Api iniciada na porta: " + port);
})

interface iUser{
    id: number
    name: string
    email: string
    isActive: boolean
}
let array: iUser[] = [
    {email: 'teste@', id: 20, isActive: true, name: 'teste'},
    {email: 'teste2@', id: 22, isActive: false, name: 'teste2'}
]

app.get('/users', (req, res) => {
    res.json(array)
})



function getById1<T extends { id: number }>(items: T[], id: number): T | undefined{
    return items.find(item => item.id===id)
}
app.get('/users/:id', (req, res) => {
    res.json(getById1(array, parseInt(req.params.id)))
})
        
function getById2<T extends { email:string }>(items: T[], email:string ): T | undefined{
    return items.find(item => item.email===email)
}
app.get('/usersemail/:email', (req, res) => {
    res.json(getById2(array,(req.params.email)))
})



app.post('/users', (req, res) => {
    res.json(array.push(req.body))
})


app.put('/users/:id', (req, res) => {
    res.json('atualizacao com sucesso')
})


app.delete('/users/:id', (req,res) => {
    res.json('usuario removido')    
})