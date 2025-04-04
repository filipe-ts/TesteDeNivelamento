<script setup lang="ts">
const props = defineProps({
    operadoras: {
      type: Array<any>,
      required: true
    }
  }
)

const prettyCNPJ = (cnpj: string) => {
  return cnpj.slice(0,2) + "." + cnpj.slice(2,5) + "." + cnpj.slice(5,8) + "/" + cnpj.slice(8,12) + "-" + cnpj.slice(12,14);
}
</script>

<template>
<ol v-if="props.operadoras.length > 0" class="list">
        <li v-for="operadora in operadoras" :key="operadora.CNPJ">
          <div class="cnpj">
             CNPJ: {{prettyCNPJ(operadora.CNPJ.toString())}}
          </div>
          <div class="razaoSocial">
            Razão Social: {{operadora.Razao_Social}}
          </div>
          <div :class="operadora.Nome_Fantasia ? 'nomeFantasia' : 'none' "></div>
           Nome Fantasia: {{operadora.Nome_Fantasia}}
        </li>
      </ol>
</template>

<style scoped>

</style>