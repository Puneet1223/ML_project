
              train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

              train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
              test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

              logging.info("Ingestion of the data is completed")
              
              return(
                   self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path