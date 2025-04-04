<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, computed, watch } from 'vue'
import ANSSearchBar from "@/components/ANSSearchBar.vue";
import ANSBtn from "@/components/ANSBtn.vue";
import { searchTypes } from "@/model/searchTypes.ts";
import { fetchOperadoras } from "@/services/fetchOperadoras.ts";

const searchType = ref(searchTypes.CNPJ);
const searchString = ref("");

const response = ref<any | null>(null);
const error = ref(null);
const hasResults = computed(() => {
  return response.value !== null
});

const operadoras = ref<Array<any>>([]);

const printStates = () => {
  console.log(searchType.value)
  console.log(searchString.value)
};

watch(hasResults, () => {console.log(hasResults.value)});
watch(response, (newValue) => {
  console.log(typeof newValue === "string");
  console.log(newValue);
  newValue.operadoras !== undefined? operadoras.value = newValue.operadoras : null;
  console.log(operadoras.value);
});

const prettyCNPJ = (cnpj: string) => {
  return cnpj.slice(0,2) + "." + cnpj.slice(2,5) + "." + cnpj.slice(5,8) + "/" + cnpj.slice(8,12) + "-" + cnpj.slice(12,14);
}
</script>

<template>
  <header>
    Busca ANS
  </header>
  <search>
      <ANSSearchBar @searchType="(msg) => searchType = msg"
                    @searchString="(msg) => searchString = msg"
      />
      <ANSBtn :search-string="searchString"
              :search-type="searchType"
              @response="(msg) => response = msg"
              @error="(msg) => error = msg" />
  </search>
  <section>
      <ol v-if="operadoras.length > 0" class="list">
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
  </section>

<!--      <nav>-->
<!--        <RouterLink to="/">Home</RouterLink>-->
<!--        <RouterLink to="/about">About</RouterLink>-->
<!--      </nav>-->
<!--  <RouterView />-->
</template>

<style scoped>
.none{
  display: none;
}
</style>
