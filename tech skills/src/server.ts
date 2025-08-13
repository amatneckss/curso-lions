import express from 'express'
import validationBr from 'validation-br'

const app = express();
const port: number = 3000;

app.use(express.json());
	
app.listen(port, () => {
    console.log("Api iniciada na porta: " + port);
});


app.get('/valida-cpf/:cpf',(req: Request, res:Response) => {
    if (validationBr.isCPF(req.params.cpf)) {
        return res.send('CPF valido');
    } else {
        return res.send('CPF invalido');
    }
})

app.get('/valida-cnpj/:cnpj',(req: Request, res:Response) => {
    if (validationBr.isCNPJ(req.params.cnpj)) {
        return res.send('CNPJ valido');
    } else {
        return res.send('CNPJ invalido');
    }
})

app.get('/valida-cnh/:cnh',(req: Request, res:Response) => {
    if (validationBr.isCNH(req.params.iscnh)) {
        return res.send('CNH valido');
    } else {
        return res.send('CNH invalido');
    }
})
