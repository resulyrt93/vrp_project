import React from 'react';
import {List} from "antd";

const ResultList = ({resultData}) => {
  return (
    <div>
      <List
        itemLayout="horizontal"
        dataSource={resultData.routes}
        renderItem={item => (
          <List.Item>
            <List.Item.Meta
              title={<span>Delivery Duration : {item.delivery_duration}</span>}
              description={<span>Jobs : {item.jobs.map((job, index) => {
                return index < item.jobs.length - 1 ? `${job} -> ` : job
              })}</span>}
            />
          </List.Item>
        )}
      />
    </div>
  );
};

export default ResultList;