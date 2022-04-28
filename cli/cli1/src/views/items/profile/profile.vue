<template>
  <v-container
      id="user-profile-view"
      fluid
      tag="section"
      style=""
  >
    <v-row justify="center">
      <v-col
          cols="12"
          md="8"
      >
        <v-card
            icon="mdi-account-outline"
            style="margin-left: 33px;margin-top: 10px"
        >
          <template #title>
            Edit Profile — <small class="text-body-1">Complete your profile</small>
          </template>

          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col
                    cols="12"
                    md="4"
                >
                  <v-text-field
                      disabled
                      label="Company (disabled)"
                  />
                </v-col>

                <v-col
                    cols="12"
                    md="4"
                >
                  <v-text-field
                      color="purple"
                      label="User Name"
                  />
                </v-col>

                <v-col
                    cols="12"
                    md="4"
                >
                  <v-text-field
                      color="purple"
                      label="Email Address"
                  />
                </v-col>

                <v-col
                    cols="12"
                    md="6"
                >
                  <v-text-field
                      color="purple"
                      label="First Name"
                  />
                </v-col>

                <v-col
                    cols="12"
                    md="6"
                >
                  <v-text-field
                      color="purple"
                      label="Last Name"
                  />
                </v-col>

                <v-col cols="12">
                  <v-text-field
                      color="purple"
                      label="Adress"
                  />
                </v-col>

                <v-col
                    cols="12"
                    md="4"
                >
                  <v-text-field
                      color="purple"
                      label="City"
                  />
                </v-col>

                <v-col
                    cols="12"
                    md="4"
                >
                  <v-text-field
                      color="purple"
                      label="Country"
                  />
                </v-col>

                <v-col
                    cols="12"
                    md="4"
                >
                  <v-text-field
                      color="purple"
                      label="Postal Code"
                      type="number"
                  />
                </v-col>

                <v-col cols="12">
                  <v-textarea
                      color="purple"
                      label="About Me"
                      value="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                  />
                </v-col>

                <v-col
                    cols="12"
                    class="text-right"
                >
                  <v-btn
                      color="primary"
                      min-width="150"
                  >
                    Update Profile
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-card>
      </v-col>
      <v-col
          cols="12"
          md="4"
      >
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
export default {
  name: "profile",
  beforeCreate() {
    this.$store.commit("getindex",3)
  },
}
</script>

<!--<template>-->
<!--  <div style="margin-left: 40px">-->
<!--    <h2>这里为个人界面</h2>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
<!--  name: "profile",-->
<!--  beforeCreate() {-->
<!--    this.$store.commit("getindex",3)-->
<!--  },-->
<!--}-->

<!--</script>-->

<!--<style scoped>-->

<!--</style>-->
