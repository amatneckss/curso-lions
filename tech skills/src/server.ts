import express from 'express'
import validationBr from 'validation-br'
import {promises} from 'dns';
import cep from 'cep-promise'


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
    if (validationBr.isCNH(req.params.cnh)) {
        return res.send('CNH valido');
    } else {
        return res.send('CNH invalido');
    }
})

app.get('/valida-cep/:cep', async (req: Request<{ cep: string | number }>, res: Response) => {
    const dados: any = await cep(req.params.cep)
                            .then((data) => { return data })
                            .catch((err) => { return err });
    return res.json({ dados:  dados })
});

interface iPessoa {
    CPF: number,
    nome: string,
    RG: number 
}

interface iEndereco {
    CEP: number,
    rua: string,
    bairro: string,
    cidade: string,
    estado: string
}

interface iCliente extends iPessoa, iEndereco {
    email: string
}

let array: iCliente []=[
    { CPF: 11111111111, nome: 'teste', RG: 222222222, CEP: 3333333333, rua: 'rua tal', bairro: 'bairro tal', cidade: 'cidade tal', estado: 'estado tal',  email: 'teste@'}
]
app.get('/clientes', (rec, res) => {
    res.json(array)
})