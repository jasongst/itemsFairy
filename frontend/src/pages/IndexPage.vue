<template>
  <div
    style="height: 100vh; width: 100%; padding-top: 30px; padding-bottom: 30px"
  >
    <div class="row q-gutter-x-lg">
      <div class="stat-card col-3 bg-secondary text-tertiary">
        Produits trouvés
        <div class="subtitle text-white">293</div>
      </div>
      <div class="stat-card col-3 bg-secondary"></div>
      <div class="stat-card col-3 bg-secondary"></div>
    </div>
    <div class="footer text-white">
      Made with ❤️ by <span class="text-weight-bold">Diez1</span>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.footer {
  position: absolute;
  bottom: 40px;
}

.stat-card {
  height: 90px;
  border-radius: 14px;
  padding: 18px;
}
</style>
