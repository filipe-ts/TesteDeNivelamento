<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, computed, watch } from 'vue'
import ANSSearchBar from "@/components/ANSSearchBar.vue";
import ANSBtn from "@/components/ANSBtn.vue";
import ANSList from "@/components/ANSList.vue";
import ANSPageNav from "@/components/ANSPageNav.vue";
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
const pagination = ref({
  current_page: 1,
  has_next: false,
  has_previous: false,
  per_page: 20,
  total_items: 0,
  total_pages: 1
});


const hasMultiplePages = computed(() => {
  return pagination.value.total_pages > 1;
})

const printStates = () => {
  console.log(searchType.value)
  console.log(searchString.value)
};

watch(response, (newValue) => {
  if (newValue.operadoras !== undefined){
     operadoras.value = newValue.operadoras;
     pagination.value = newValue.pagination;
     console.log(pagination.value.current_page);
  }
});


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
  <ANSPageNav :search-string="searchString"
              :search-type="searchType"
              :pagination="pagination"
              @response="(msg) => response = msg" />
  <section>
      <ANSList :operadoras="operadoras" />
  </section>


<!--      <nav>-->
<!--        <RouterLink to="/">Home</RouterLink>-->
<!--        <RouterLink to="/about">About</RouterLink>-->
<!--      </nav>-->
<!--  <RouterView />-->
</template>

<style scoped>
.transparent{
  opacity: 0;
}

</style>
