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

const prettyCNPJ = (cnpj: string) => {
  return cnpj.slice(0,2) + "." + cnpj.slice(2,5) + "." + cnpj.slice(5,8) + "/" + cnpj.slice(8,12) + "-" + cnpj.slice(12,14);
}
</script>

<template>
<ol v-if="props.operadoras.length > 0" class="list">
        <li :class="index%2 === 0 ? 'par' : 'impar' " v-for="(operadora, index) in operadoras" :key="operadora.CNPJ">
          <div class="cnpj">
             CNPJ: {{prettyCNPJ(operadora.CNPJ.toString())}}
          </div>
          <div class="razaoSocial">
            Razão Social: {{operadora.Razao_Social}}
          </div>
          <div :class="operadora.Nome_Fantasia !== '' ? 'nomeFantasia' : 'none' ">
           Nome Fantasia: {{operadora.Nome_Fantasia}}
          </div>
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

.impar, .par{
  padding: 0.5rem 1rem 0.5rem 1rem;
}

.impar{
  background-color: #202020;
}

.semResultados{
  display: flex;
  justify-self: center;
  color: #9e9e9e;
}
</style>