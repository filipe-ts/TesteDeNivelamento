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

const isSearchEnable = ref(false);
const searchButtonRef = ref<HTMLElement | null>(null);

const isFirstLoad = ref(true);

const operadoras = ref<Array<any>>([]);
const pagination = ref({
  current_page: 1,
  has_next: false,
  has_previous: false,
  per_page: 20,
  total_items: 0,
  total_pages: 1
});

watch(response, (newValue) => {
  if (newValue.operadoras !== undefined){
     isFirstLoad.value = false;
     operadoras.value = newValue.operadoras;
     pagination.value = newValue.pagination;
     console.log(pagination.value.current_page);
  }
});

const fetchData = () => {
  if (isSearchEnable.value) {
    searchButtonRef.value!.click();
  }
}

</script>

<template>
  <header class="header">
    <h1>Busca ANS</h1>
  </header>
  <search class="searchContainer">
      <ANSSearchBar @searchType="(msg) => searchType = msg"
                    @searchString="(msg) => searchString = msg"
                    @searchRequested="fetchData"
      />
      <ANSBtn class="btn"
              ref="searchButtonRef"
              :search-string="searchString"
              :search-type="searchType"
              @response="(msg) => response = msg"
              @error="(msg) => error = msg"
              @searchEnable="(msg) => isSearchEnable = msg" />
  </search>
  <ANSPageNav class="pageNav"
              :search-string="searchString"
              :search-type="searchType"
              :pagination="pagination"
              @response="(msg) => response = msg" />
  <section>
      <ANSList :operadoras="operadoras" :is-fist-time="isFirstLoad" />
  </section>
  <ANSPageNav class="pageNav"
              :search-string="searchString"
              :search-type="searchType"
              :pagination="pagination"
              @response="(msg) => response = msg" />


<!--      <nav>-->
<!--        <RouterLink to="/">Home</RouterLink>-->
<!--        <RouterLink to="/about">About</RouterLink>-->
<!--      </nav>-->
<!--  <RouterView />-->
</template>

<style scoped>
.header h1{
  font-weight: 800;
  color: #55ec93;
}
.transparent{
  opacity: 0;
}

.searchContainer{
  display: flex;
  width: 100%;
  height: 5rem;
  align-items: end;
}

.btn{
  height: 50%;
}

.pageNav{
  display: flex;
  justify-self: center;
  margin: 1rem;
}
</style>
