from datetime import datetime
from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model, UserMixin):
    __tablename__ = 'cp_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    username = db.Column(db.String(20), comment='用户名')
    realname = db.Column(db.String(20), comment='真实名字')
    mobile = db.Column(db.String(11), comment='电话号码')
    avatar = db.Column(db.String(255), comment='头像', default="/static/admin/admin/images/avatar.jpg")
    comment = db.Column(db.String(255), comment='备注')
    password_hash = db.Column(db.String(128), comment='哈希密码')
    enable = db.Column(db.Integer, default=0, comment='启用')
    dept_id = db.Column(db.Integer, comment='部门id')

    role = db.relationship('RoleModel', secondary="rt_user_role", backref=db.backref('user'), lazy='dynamic')

    def set_password(self, password):
        """设置密码，对密码进行加密存储"""
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        """校验密码方法"""
        return check_password_hash(self.password_hash, password)

    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

# 创建中间表
user_role = db.Table(
    "rt_user_role",  # 中间表名称
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, comment='标识'),  # 主键
    db.Column("user_id", db.Integer, db.ForeignKey("cp_user.id"), comment='用户编号'),  # 属性 外键
    db.Column("role_id", db.Integer, db.ForeignKey("rt_role.id"), comment='角色编号'),  # 属性 外键
)

# 创建中间表
role_power = db.Table(
    "rt_role_power",  # 中间表名称
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, comment='标识'),  # 主键
    db.Column("power_id", db.Integer, db.ForeignKey("rt_power.id"), comment='用户编号'),  # 属性 外键
    db.Column("role_id", db.Integer, db.ForeignKey("rt_role.id"), comment='角色编号'),  # 属性 外键
)

class RoleModel(db.Model):
    __tablename__ = 'rt_role'
    id = db.Column(db.Integer, primary_key=True, comment='角色ID')
    name = db.Column(db.String(255), comment='角色名称')
    code = db.Column(db.String(255), comment='角色标识')
    enable = db.Column(db.Boolean, comment='是否启用')
    comment = db.Column(db.String(255), comment='备注')
    details = db.Column(db.String(255), comment='详情')
    sort = db.Column(db.Integer, comment='排序')

    power = db.relationship('RightModel', secondary="rt_role_power", backref=db.backref('role'))

class RightModel(db.Model):
    __tablename__ = 'rt_power'
    id = db.Column(db.Integer, primary_key=True, comment='权限编号')
    name = db.Column(db.String(255), comment='权限名称')
    type = db.Column(db.SMALLINT, comment='权限类型')
    code = db.Column(db.String(30), comment='权限标识')
    url = db.Column(db.String(255), comment='权限路径')
    open_type = db.Column(db.String(10), comment='打开方式')
    parent_id = db.Column(db.Integer, db.ForeignKey("rt_power.id"), comment='父类编号')
    icon = db.Column(db.String(128), comment='图标')
    sort = db.Column(db.Integer, comment='排序')
    enable = db.Column(db.Boolean, comment='是否开启')

    parent = db.relationship("RightModel", remote_side=[id])  # 自关联


class DepartmentModel(db.Model):
    __tablename__ = 'cp_dept'
    id = db.Column(db.Integer, primary_key=True, comment="部门ID")
    parent_id = db.Column(db.Integer, comment="父级编号")
    dept_name = db.Column(db.String(50), comment="部门名称")
    leader = db.Column(db.String(50), comment="负责人")
    phone = db.Column(db.String(20), comment="联系方式")
    email = db.Column(db.String(50), comment="邮箱")
    status = db.Column(db.Boolean, comment='状态(1开启,0关闭)')
    comment = db.Column(db.Text, comment="备注")
    address = db.Column(db.String(255), comment="详细地址")
    sort = db.Column(db.Integer, comment="排序")

    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')


class LogModel(db.Model):
    __tablename__ = 'lg_logging'
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(10))
    uid = db.Column(db.Integer, default=None)
    url = db.Column(db.String(255))
    desc = db.Column(db.Text)
    ip = db.Column(db.String(255))
    success = db.Column(db.Boolean, default=True)
    user_agent = db.Column(db.Text)

    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
