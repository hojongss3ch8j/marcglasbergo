# Generated by Django 3.2.3 on 2021-06-01 17:13

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.CharField(default=uuid.uuid4, help_text='Id', max_length=255, primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人Id', max_length=255, null=True, verbose_name='修改人Id')),
                ('modifier_id', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('dept_belong_id', models.CharField(blank=True, help_text='数据归属部门', max_length=255, null=True, verbose_name='数据归属部门')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('username', models.CharField(db_index=True, help_text='用户账号', max_length=150, unique=True, verbose_name='用户账号')),
                ('email', models.EmailField(blank=True, help_text='邮箱', max_length=255, null=True, verbose_name='邮箱')),
                ('mobile', models.CharField(blank=True, help_text='电话', max_length=255, null=True, verbose_name='电话')),
                ('avatar', models.CharField(blank=True, help_text='头像', max_length=255, null=True, verbose_name='头像')),
                ('name', models.CharField(help_text='姓名', max_length=40, verbose_name='姓名')),
                ('gender', models.IntegerField(blank=True, choices=[(0, '女'), (1, '男')], help_text='性别', null=True, verbose_name='性别')),
                ('creator', models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'system_users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, help_text='Id', max_length=255, primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人Id', max_length=255, null=True, verbose_name='修改人Id')),
                ('modifier_id', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('dept_belong_id', models.CharField(blank=True, help_text='数据归属部门', max_length=255, null=True, verbose_name='数据归属部门')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('name', models.CharField(help_text='部门名称', max_length=64, verbose_name='部门名称')),
                ('sort', models.IntegerField(default=1, help_text='显示排序', verbose_name='显示排序')),
                ('owner', models.CharField(blank=True, help_text='负责人', max_length=32, null=True, verbose_name='负责人')),
                ('phone', models.CharField(blank=True, help_text='联系电话', max_length=32, null=True, verbose_name='联系电话')),
                ('email', models.EmailField(blank=True, help_text='邮箱', max_length=32, null=True, verbose_name='邮箱')),
                ('status', models.IntegerField(blank=True, choices=[(0, '禁用'), (1, '启用')], default=1, help_text='部门状态', null=True, verbose_name='部门状态')),
                ('creator', models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('parent', models.ForeignKey(blank=True, db_constraint=False, default=False, help_text='上级部门', null=True, on_delete=django.db.models.deletion.CASCADE, to='system.dept', verbose_name='上级部门')),
            ],
            options={
                'verbose_name': '部门表',
                'verbose_name_plural': '部门表',
                'db_table': 'system_dept',
            },
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, help_text='Id', max_length=255, primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人Id', max_length=255, null=True, verbose_name='修改人Id')),
                ('modifier_id', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('dept_belong_id', models.CharField(blank=True, help_text='数据归属部门', max_length=255, null=True, verbose_name='数据归属部门')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('code', models.CharField(blank=True, help_text='编码', max_length=100, null=True, unique=True, verbose_name='编码')),
                ('name', models.CharField(blank=True, help_text='名称', max_length=100, null=True, verbose_name='名称')),
                ('status', models.IntegerField(choices=[(0, '禁用'), (1, '启用')], default=1, help_text='状态', verbose_name='状态')),
                ('sort', models.IntegerField(blank=True, default=1, help_text='显示排序', null=True, verbose_name='显示排序')),
                ('remark', models.CharField(blank=True, help_text='备注', max_length=2000, null=True, verbose_name='备注')),
                ('creator', models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('parent', models.ForeignKey(blank=True, db_constraint=False, help_text='父级', null=True, on_delete=django.db.models.deletion.PROTECT, to='system.dictionary', verbose_name='父级')),
            ],
            options={
                'verbose_name': '字典表',
                'verbose_name_plural': '字典表',
                'db_table': 'system_dictionary',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, help_text='Id', max_length=255, primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人Id', max_length=255, null=True, verbose_name='修改人Id')),
                ('modifier_id', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('dept_belong_id', models.CharField(blank=True, help_text='数据归属部门', max_length=255, null=True, verbose_name='数据归属部门')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('icon', models.CharField(blank=True, help_text='菜单图标', max_length=64, null=True, verbose_name='菜单图标')),
                ('name', models.CharField(help_text='菜单名称', max_length=64, verbose_name='菜单名称')),
                ('sort', models.IntegerField(blank=True, default=1, help_text='显示排序', null=True, verbose_name='显示排序')),
                ('is_link', models.IntegerField(choices=[(0, '否'), (1, '是')], default=0, help_text='是否外链', verbose_name='是否外链')),
                ('web_path', models.CharField(blank=True, help_text='路由地址', max_length=128, null=True, verbose_name='路由地址')),
                ('status', models.IntegerField(choices=[(0, '禁用'), (1, '启用')], default=1, help_text='菜单状态', verbose_name='菜单状态')),
                ('creator', models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('parent', models.ForeignKey(blank=True, db_constraint=False, help_text='上级菜单', null=True, on_delete=django.db.models.deletion.CASCADE, to='system.menu', verbose_name='上级菜单')),
            ],
            options={
                'verbose_name': '菜单表',
                'verbose_name_plural': '菜单表',
                'db_table': 'system_menu',
            },
        ),
        migrations.CreateModel(
            name='SysDictionarylist',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, help_text='Id', max_length=255, primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人Id', max_length=255, null=True, verbose_name='修改人Id')),
                ('modifier_id', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('dept_belong_id', models.CharField(blank=True, help_text='数据归属部门', max_length=255, null=True, verbose_name='数据归属部门')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('code', models.CharField(blank=True, help_text='编码', max_length=100, null=True, verbose_name='编码')),
                ('label', models.CharField(blank=True, help_text='显示名称', max_length=100, null=True, verbose_name='显示名称')),
                ('value', models.CharField(blank=True, help_text='实际值', max_length=100, null=True, verbose_name='实际值')),
                ('status', models.IntegerField(choices=[(0, '禁用'), (1, '启用')], default=1, help_text='状态', verbose_name='状态')),
                ('remark', models.CharField(blank=True, help_text='备注', max_length=2000, null=True, verbose_name='备注')),
                ('creator', models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('dict', models.ForeignKey(blank=True, db_constraint=False, help_text='关联主表', null=True, on_delete=django.db.models.deletion.PROTECT, to='system.dictionary', verbose_name='关联主表')),
            ],
            options={
                'verbose_name': '字典详细表',
                'verbose_name_plural': '字典详细表',
                'db_table': 'system_dictionary_detail',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, help_text='Id', max_length=255, primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人Id', max_length=255, null=True, verbose_name='修改人Id')),
                ('modifier_id', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('dept_belong_id', models.CharField(blank=True, help_text='数据归属部门', max_length=255, null=True, verbose_name='数据归属部门')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('name', models.CharField(help_text='角色名称', max_length=64, verbose_name='角色名称')),
                ('key', models.CharField(help_text='权限字符', max_length=64, verbose_name='权限字符')),
                ('sort', models.IntegerField(default=1, help_text='角色顺序', verbose_name='角色顺序')),
                ('status', models.IntegerField(choices=[(0, '禁用'), (1, '启用')], default=1, help_text='角色状态', verbose_name='角色状态')),
                ('admin', models.IntegerField(choices=[(0, '否'), (1, '是')], default=0, help_text='是否为admin', verbose_name='是否为admin')),
                ('data_range', models.IntegerField(choices=[(0, '仅本人数据权限'), (1, '本部门及以下数据权限'), (2, '本部门数据权限'), (3, '全部数据权限'), (4, '自定数据权限')], default=0, help_text='数据权限范围', verbose_name='数据权限范围')),
                ('remark', models.TextField(blank=True, help_text='备注', null=True, verbose_name='备注')),
                ('creator', models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('dept', models.ManyToManyField(db_constraint=False, help_text='关联部门', to='system.Dept', verbose_name='数据权限-关联部门')),
                ('menu', models.ManyToManyField(db_constraint=False, help_text='关联菜单', to='system.Menu', verbose_name='关联菜单')),
            ],
            options={
                'verbose_name': '角色表',
                'verbose_name_plural': '角色表',
                'db_table': 'system_role',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, help_text='Id', max_length=255, primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人Id', max_length=255, null=True, verbose_name='修改人Id')),
                ('modifier_id', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('dept_belong_id', models.CharField(blank=True, help_text='数据归属部门', max_length=255, null=True, verbose_name='数据归属部门')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('name', models.CharField(help_text='岗位名称', max_length=64, verbose_name='岗位名称')),
                ('code', models.CharField(help_text='岗位编码', max_length=32, verbose_name='岗位编码')),
                ('sort', models.IntegerField(default=1, help_text='岗位顺序', verbose_name='岗位顺序')),
                ('status', models.IntegerField(choices=[(0, '离职'), (1, '在职')], default=1, help_text='岗位状态', verbose_name='岗位状态')),
                ('creator', models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '岗位表',
                'verbose_name_plural': '岗位表',
                'db_table': 'system_post',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, help_text='Id', max_length=255, primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人Id', max_length=255, null=True, verbose_name='修改人Id')),
                ('modifier_id', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('dept_belong_id', models.CharField(blank=True, help_text='数据归属部门', max_length=255, null=True, verbose_name='数据归属部门')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('name', models.CharField(help_text='权限名称', max_length=64, verbose_name='权限名称')),
                ('value', models.CharField(help_text='权限值', max_length=64, verbose_name='权限值')),
                ('creator', models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '权限表',
                'verbose_name_plural': '权限表',
                'db_table': 'system_permission',
            },
        ),
        migrations.CreateModel(
            name='MenuPermission',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, help_text='Id', max_length=255, primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人Id', max_length=255, null=True, verbose_name='修改人Id')),
                ('modifier_id', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('dept_belong_id', models.CharField(blank=True, help_text='数据归属部门', max_length=255, null=True, verbose_name='数据归属部门')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('name', models.CharField(help_text='名称', max_length=64, verbose_name='名称')),
                ('value', models.CharField(help_text='权限值', max_length=64, verbose_name='权限值')),
                ('api', models.CharField(help_text='接口地址', max_length=64, verbose_name='接口地址')),
                ('method', models.IntegerField(blank=True, default=0, help_text='接口请求方法', null=True, verbose_name='接口请求方法')),
                ('creator', models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('menu', models.ForeignKey(help_text='关联菜单', on_delete=django.db.models.deletion.CASCADE, to='system.menu', verbose_name='关联菜单')),
            ],
            options={
                'verbose_name': '菜单权限表',
                'verbose_name_plural': '菜单权限表',
                'db_table': 'system_menu_permission',
            },
        ),
        migrations.AddField(
            model_name='users',
            name='dept',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='关联部门', null=True, on_delete=django.db.models.deletion.CASCADE, to='system.dept', verbose_name='所属部门'),
        ),
        migrations.AddField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='users',
            name='post',
            field=models.ManyToManyField(db_constraint=False, help_text='关联岗位', to='system.Post', verbose_name='关联岗位'),
        ),
        migrations.AddField(
            model_name='users',
            name='role',
            field=models.ManyToManyField(db_constraint=False, help_text='关联角色', to='system.Role', verbose_name='关联角色'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
