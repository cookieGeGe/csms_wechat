import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/views/Login'
import Main from '@/views/Main'
import Company from '@/views/company/Company'
import CompanyView from '@/views/company/CompanyView'
import Project from '@/views/project/Project'
import ProjectView from '@/views/project/ProjectView'
import Labor from '@/views/labor/Labor'

import Help from '@/views/help/Help'
import helpView from '@/views/help/helpView'
import guarantee from '@/views/guarantee/guarantee'
import guaranteeView from '@/views/guarantee/guaranteeView'

import bank from '@/views/bank/bank'
import bankView from '@/views/bank/bankView'

import wage from '@/views/wage/wage'
import wageView from '@/views/wage/wageView'

import Search from '@/components/areas/Search'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/Main',
      name: 'Main',
      component: Main
    },
    {
      path: '/Search',
      name: 'Search',
      component: Search
    },
    {
      path: '/Company',
      name: 'Company',
      component: Company
    },
    {
      path: '/Project',
      name: 'Project',
      component: Project
    },
    {
      path: '/Labor',
      name: 'Labor',
      component: Labor
    },
    {
      path: '/CompanyView',
      name: 'CompanyView',
      component: CompanyView
    },
    {
      path: '/ProjectView',
      name: 'ProjectView',
      component: ProjectView
    },

    {
      path: '/Help',
      name: 'Help',
      component: Help
    },
    {
      path: '/helpView',
      name: 'helpView',
      component: helpView
    },
    {
      path: '/Guarantee',
      name: 'Guarantee',
      component: guarantee
    },
    {
      path: '/GuaView',
      name: 'GuaView',
      component: guaranteeView
    },
    {
      path: '/bank',
      name: 'bank',
      component: bank
    },
    {
      path: '/bankView',
      name: 'bankView',
      component: bankView
    },
    {
      path: '/salary',
      name: 'salary',
      component: wage
    },
    {
      path: '/salaryView',
      name: 'salaryView',
      component: wageView
    },
  ]
})
