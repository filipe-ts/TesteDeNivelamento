<script setup lang="ts">
import {ref} from "vue";

const props = defineProps({
    operadoras: {
      type: Array<any>,
      required: true
    },
    isFistTime: {
      type: Boolean,
      required: true
    }
  }
);

const showDetailArr = ref<Array<Boolean>>(new Array<Boolean>(props.operadoras.length).fill(false));

const updatDetailArr = (index: number) => {
  let temp = showDetailArr.value.slice();
  temp[index] = !temp[index];
  showDetailArr.value = temp;
}

const prettyCNPJ = (cnpj: string) => {
  return cnpj.slice(0,2) + "." + cnpj.slice(2,5) + "." + cnpj.slice(5,8) + "/" + cnpj.slice(8,12) + "-" + cnpj.slice(12,14);
}

const prettyCEP = (cep: string) => {
  return cep.slice(0,2) + "." + cep.slice(2,5) + "-" + cep.slice(5,8);
}
</script>

<template>
<ol v-if="props.operadoras.length > 0" class="list">
        <li :class="index%2 === 0 ? 'par' : 'impar' " v-for="(operadora, index) in operadoras" :key="operadora.CNPJ">
          <div class="item">
            <div class="cnpj">
             CNPJ: {{prettyCNPJ(operadora.CNPJ.toString())}} | Registro na ANS: {{operadora.Registro_ANS}}
            </div>
            <div class="razaoSocial">
              Razão Social: {{operadora.Razao_Social}}
            </div>
            <div :class="operadora.Nome_Fantasia !== '' ? 'nomeFantasia' : 'none' ">
             Nome Fantasia: {{operadora.Nome_Fantasia}}
            </div>
          </div>
          <button class="btn" @click="updatDetailArr(index)">
            Mostrar Detalhes
          </button>
          <div :class="showDetailArr[index] ? 'closeDetails' : 'none' " @click="updatDetailArr(index)">
            X
          </div>
          <ul :class="showDetailArr[index] ? 'details' : 'none' ">
            <li class="item">
              Nº de Registro na ANS: {{operadora.Registro_ANS}}
            </li>
            <li :class="operadora.Data_Registro_ANS ? 'item' : 'none' ">
              Data de registro: {{operadora.Data_Registro_ANS}}
            </li>
            <li class="item">
              CNPJ: {{operadora.CNPJ}}
            </li>
            <li class="item">
              Razão Social: {{operadora.Razao_Social}}
            </li>
            <li class="item">
              Nº de Registro na ANS: {{operadora.Registro_ANS}}
            </li>
            <li :class="operadora.Nome_Fantasia ? 'item' : 'none' ">
              Nome Fantasia: {{operadora.Nome_Fantasia}}
            </li>
            <li :class="operadora.Modalidade ? 'item' : 'none' ">
              Modalidade: {{operadora.Modalidade}}
            </li>
            <li :class="operadora.Logradouro ? 'item' : 'none' ">
              Logradouro: {{operadora.Logradouro}}
            </li>
            <li class="item">
              Número: {{operadora.Numero ? operadora.Numero : 'S/Nº'}}
            </li>
            <li :class="operadora.Complemento ? 'item' : 'none' ">
              Complemento: {{operadora.Complemento}}
            </li>
            <li :class="operadora.Bairro ? 'item' : 'none' ">
              Bairro: {{operadora.Bairro}}
            </li>
            <li :class="operadora.Cidade ? 'item' : 'none' ">
              Cidade: {{operadora.Cidade}}
            </li>
            <li :class="operadora.UF ? 'item' : 'none' ">
              UF: {{operadora.UF}}
            </li>
            <li :class="operadora.CEP ? 'item' : 'none' ">
              CEP: {{prettyCEP(operadora.CEP)}}
            </li>
            <li :class="operadora.DDD ? 'item' : 'none' ">
              Telefone: {{operadora.DDD}} - {{operadora.Telefone}}
            </li>
            <li :class="operadora.Fax ? 'item' : 'none' ">
              Fax: {{operadora.Fax}}
            </li>
            <li :class="operadora.Endereco_eletronico ? 'item' : 'none' ">
              Email: {{operadora.Endereco_eletronico}}
            </li>
            <li :class="operadora.Representante ? 'item' : 'none' ">
              Representante: {{operadora.Representante}}
            </li>
            <li :class="operadora.Cargo_Representante ? 'item' : 'none' ">
              Cargo do representante: {{operadora.Cargo_Representante}}
            </li>
            <li :class="operadora.Regiao_de_Comercializacao ? 'item' : 'none' ">
              Região de comercialização: {{operadora.Regiao_de_Comercializacao}}ª
            </li>
          </ul>
        </li>

      </ol>
  <div v-if="props.operadoras.length === 0 && !props.isFistTime" class="semResultados">
    Não foram encontrados resultados para essa busca.
  </div>
</template>

<style scoped>
*{
  color: white;
}

.none{
  display: none;
}

.list{
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.item{
  display: flex;
  flex-direction: column;
  max-width: calc(100% - 10rem);
}

.details{
  position: fixed;
  right: 10%;
  left: 10%;
  top: 10%;
  bottom: 12%;
  background-color: #282828;
  padding: 1.5rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.closeDetails{
  z-index: 10;
  position: fixed;
  width: 2rem;
  height: 2rem;
  border-radius: 0.2rem;
  background-color: #7e1212;
  right: 10%;
  top: 10%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.impar, .par{
  padding: 0.5rem 1rem 0.5rem 1rem;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.impar{
  background-color: #202020;
}

.btn{
  background-color: #55ec93;
  color: #181818;

  font-weight: bold;
}

.btn:active{
  background-color: #05632c;
  color: #ffffff;
}

.semResultados{
  display: flex;
  justify-self: center;
  color: #9e9e9e;
}
</style>