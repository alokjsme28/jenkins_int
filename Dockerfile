FROM centos

RUN yum install python36 -y

RUN pip3 install pandas

RUN pip3 install scikit-learn

COPY marks.csv  /
COPY marks.py   /

CMD python3 /marks.py