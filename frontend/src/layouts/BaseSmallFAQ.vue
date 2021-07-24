<template>
<div class="col-sm-12 col-md-8 offset-md-2">
  <h2 class="font-weight-bold my-5 text-center">Frequently Asked Questions</h2>

  <div class="accordion" role="tablist">
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-1 variant="info">What are Tasks and how many do I need?</b-button>
      </b-card-header>

      <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-card-text>
            A Task is counted every time a Zap successfully moves data or takes action for you. For example, if your Zap has an action to create new Google Contacts, each contact that is created will use one Task.
            The number of Tasks you need depends on the number of active Zaps you have and how frequently those Zaps will run to automate your workflow. Don’t worry, if you use up all your Tasks in a given month we’ll hold your Tasks until you upgrade or your monthly usage resets. If you use more than 2 million Tasks, you will be billed at a per-task rate of €0.0009.
          </b-card-text>
        </b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-2 variant="info">What are Apps?</b-button>
      </b-card-header>
      
      <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-text>
              A Task is counted every time a Zap successfully moves data or takes action for you. For example, if your Zap has an action to create new Google Contacts, each contact that is created will use one Task.
              The number of Tasks you need depends on the number of active Zaps you have and how frequently those Zaps will run to automate your workflow. Don’t worry, if you use up all your Tasks in a given month we’ll hold your Tasks until you upgrade or your monthly usage resets. If you use more than 2 million Tasks, you will be billed at a per-task rate of €0.0009.
            </b-card-text>
          </b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-3 variant="info">Do you have a free trial of your premium features?</b-button>
      </b-card-header>

      <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-card-text>
            A Task is counted every time a Zap successfully moves data or takes action for you. For example, if your Zap has an action to create new Google Contacts, each contact that is created will use one Task.
            The number of Tasks you need depends on the number of active Zaps you have and how frequently those Zaps will run to automate your workflow. Don’t worry, if you use up all your Tasks in a given month we’ll hold your Tasks until you upgrade or your monthly usage resets. If you use more than 2 million Tasks, you will be billed at a per-task rate of €0.0009.
          </b-card-text>
        </b-card-body>
      </b-collapse>
    </b-card>
  </div>
</div>
</template>
