import { request } from '@/api/service'
import { BUTTON_STATUS_NUMBER } from '@/config/button'
export const crudOptions = (vm) => {
  return {

    pageOptions: {
      compact: true
    },
    options: {
      tableType: 'vxe-table',
      rowKey: true, // 必须设置，true or false
      rowId: 'id',
      height: '100%', // 表格高度100%, 使用toolbar必须设置
      highlightCurrentRow: false,

      treeConfig: { // 树形数据配置
        children: 'children',
        hasChild: 'hasChildren',
        expandAll: true
      }
    },
    rowHandle: {
      view: {
        disabled () {
          return !vm.hasPermissions('Retrieve')
        }
      },
      edit: {
        thin: true,
        text: '编辑',
        disabled () {
          return !vm.hasPermissions('Update')
        }
      },
      remove: {
        thin: true,
        text: '删除',
        disabled () {
          return !vm.hasPermissions('Delete')
        }
      }
    },
    indexRow: { // 或者直接传true,不显示title，不居中
      title: '序号',
      align: 'center',
      width: 100
    },

    viewOptions: {
      componentType: 'form'
    },
    formOptions: {
      defaultSpan: 24 // 默认的表单 span
    },
    columns: [{
      title: '关键词',
      key: 'search',
      show: false,
      disabled: true,
      search: {
        disabled: false
      },
      form: {
        disabled: true,
        component: {
          props: {
            clearable: true
          }
        }
      },
      view: { // 查看对话框组件的单独配置
        disabled: true
      }
    },
    {
      title: 'ID',
      key: 'id',
      show: false,
      disabled: true,
      width: 90,
      form: {
        disabled: true
      }
    },
    {
      title: '父级菜单',
      key: 'parent',
      show: false,
      search: {
        disabled: true
      },
      type: 'cascader',
      dict: {
        cache: false,
        url: '/api/system/dictionary/dictionary_tree/?limit=999',
        value: 'id', // 数据字典中value字段的属性名
        label: 'label', // 数据字典中label字段的属性名
        children: 'children', // 数据字典中children字段的属性名
        getData: (url, dict) => { // 配置此参数会覆盖全局的getRemoteDictFunc
          return request({ url: url }).then(ret => {
            return [{ id: null, label: '根节点', children: ret.data.data }]
          })
        }

      },
      form: {
        component: {
          span: 12,
          props: {
            elProps: {
              clearable: true,
              showAllLevels: false, // 仅显示最后一级
              props: {
                checkStrictly: true, // 可以不需要选到最后一级
                emitPath: false,
                clearable: true
              }
            }
          }
        }
      }
    },
    {
      title: '编码',
      key: 'code',
      sortable: true,
      treeNode: true,
      search: {
        disabled: true,
        component: {
          props: {
            clearable: true
          }
        }
      },
      type: 'input',
      form: {
        editDisabled: true,
        rules: [ // 表单校验规则
          { required: true, message: '必填项' }
        ],
        component: {
          span: 12,
          props: {
            clearable: true
          }
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: '显示值',
      key: 'label',
      sortable: true,

      search: {
        disabled: false,
        component: {
          props: {
            clearable: true
          }
        }
      },

      type: 'input',
      form: {
        rules: [ // 表单校验规则
          { required: true, message: '必填项' }
        ],
        component: {
          span: 12,
          props: {
            clearable: true
          }
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },
    {
      title: '实际值',
      key: 'value',
      sortable: true,

      search: {
        disabled: true,
        component: {
          props: {
            clearable: true
          }
        }
      },

      type: 'input',
      form: {
        rules: [ // 表单校验规则
          { required: true, message: '必填项' }
        ],
        component: {
          span: 12,
          props: {
            clearable: true
          }
        },
        itemProps: {
          class: { yxtInput: true }
        }
      }
    },

    {
      title: '状态',
      key: 'status',
      sortable: true,
      search: {
        disabled: false
      },

      type: 'radio',
      dict: {
        data: BUTTON_STATUS_NUMBER
      },
      form: {
        value: 1,
        component: {
          span: 12
        }
      }
    },
    {
      title: '排序',
      key: 'sort',
      sortable: true,

      type: 'number',
      form: {
        value: 1,
        component: {
          span: 12
        }
      }
    }
    ]
  }
}