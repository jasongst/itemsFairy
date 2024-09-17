<template>
  <q-layout>
    <q-drawer v-model="drawer" show-if-above :width="350" :breakpoint="500">
      <div class="drawer-container">
        <div class="q-ma-lg text-white text-center">
          <div class="q-pa-sm">
            <img class="logo" src="../assets/itemsfairy.png" />
          </div>
          <div class="menu-list q-pl-md q-mr-md">
            <div class="hr q-mb-md"></div>
            <div class="menu-item menu-item__active">
              <div class="icon-container bg-primary">
                <q-icon
                  style="position: relative; top: 5px"
                  name="notifications_active"
                  size="24px"
                />
              </div>
              <div class="self-center q-ml-md">Alertes</div>
            </div>
          </div>
        </div>
      </div>
    </q-drawer>
    <q-page-container>
      <q-page>
        <router-view />
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
const drawer = true;
</script>

<style scoped>
:deep(.q-drawer) {
  background-color: transparent;
}

.logo {
  width: 100%;
}

.hr {
  height: 1px;
  background: rgb(235, 235, 235);
  background: linear-gradient(
    90deg,
    rgba(235, 235, 235, 0.1) 0%,
    rgba(255, 255, 255, 0.35) 50%,
    rgba(235, 235, 235, 0.1) 100%
  );
}

.drawer-container {
  overflow-y: hidden;
  position: relative;
  top: 30px;
  height: calc(100% - 60px);
  width: 300px !important;
  margin: 0 auto;
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 14px;
}

.menu-item {
  height: 58px;
  cursor: pointer;
  display: flex;
}

.menu-item__active {
  background-color: rgb(26, 31, 55);
  padding: 0.675rem 0.8rem 0.675rem 1rem;
  border-radius: 0.9375rem;
}

.icon-container {
  height: 100%;
  width: 36px;
  border-radius: 0.75rem;
}
</style>
