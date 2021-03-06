"""empty message

Revision ID: dcbdb7e94810
Revises: 
Create Date: 2018-05-03 13:58:54.022000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dcbdb7e94810'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_install_order')
    op.drop_table('quote')
    op.drop_table('author')
    op.drop_table('t_customer')
    op.drop_table('t_goods')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_goods',
    sa.Column('FInterID', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('FCreator', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('FCreateTime', mysql.DATETIME(), nullable=True),
    sa.Column('FModifier', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('FModifyTime', mysql.DATETIME(), nullable=True),
    sa.Column('Code', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('SupplierID', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('Note', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('FInterID'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('t_customer',
    sa.Column('FInterID', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('FCreator', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('FCreateTime', mysql.DATETIME(), nullable=True),
    sa.Column('FModifier', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('FModifyTime', mysql.DATETIME(), nullable=True),
    sa.Column('Name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('FullName', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('Fax', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Tel', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Address', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('Note', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('FInterID'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('author',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('first', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('last', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('age', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('quote',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('content', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('author_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('posted_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], [u'author.id'], name=u'quote_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('t_install_order',
    sa.Column('FInterID', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('FCreator', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('FCreateTime', mysql.DATETIME(), nullable=True),
    sa.Column('FModifier', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('FModifyTime', mysql.DATETIME(), nullable=True),
    sa.Column('OrderNo', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Goods_ID', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('Customer_ID', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('Qty', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('Tel', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Address', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('Note', mysql.VARCHAR(length=200), nullable=True),
    sa.ForeignKeyConstraint(['Customer_ID'], [u't_customer.FInterID'], name=u't_install_order_ibfk_2'),
    sa.ForeignKeyConstraint(['Goods_ID'], [u't_goods.FInterID'], name=u't_install_order_ibfk_1'),
    sa.PrimaryKeyConstraint('FInterID'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    # ### end Alembic commands ###
